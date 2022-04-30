package com.wsei.lab2.controllers;

import com.wsei.lab2.models.UserEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

import static java.util.Map.entry;

@RestController
public class UserController {
    Map<Integer, UserEntity> users = new HashMap<>();

    @GetMapping("/users")
    Collection<UserEntity> getUsers() {
        return users.values();
    }

    @GetMapping("/users/{id}/get")
    UserEntity getUser(@PathVariable("id") int id) {
        return users.get(id);
    }

    @GetMapping("/users/{id}/remove")
    UserEntity removeUser(@PathVariable("id") int id) {
        return users.remove(id);
    }

    @GetMapping("/users/add")
    UserEntity addUser(@RequestParam("name") String name, @RequestParam("age") int age) {
        UserEntity user = new UserEntity(name, age);
        users.put(users.size(), user);
        return user;
    }
}
